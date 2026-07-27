# Last updated: 7/27/2026, 3:11:08 PM
1class Solution(object):
2    def mySqrt(self, x):
3        if x < 2:
4            return x
5
6        left, right = 1, x
7
8        while left <= right:
9            mid = (left + right) // 2
10
11            if mid * mid == x:
12                return mid
13            elif mid * mid < x:
14                left = mid + 1
15            else:
16                right = mid - 1
17
18        return right