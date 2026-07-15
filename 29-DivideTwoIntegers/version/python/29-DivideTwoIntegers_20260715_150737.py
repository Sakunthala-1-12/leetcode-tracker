# Last updated: 7/15/2026, 3:07:37 PM
1class Solution(object):
2    def divide(self, dividend, divisor):
3        INT_MAX = 2**31 - 1
4        INT_MIN = -2**31
5
6        if dividend == INT_MIN and divisor == -1:
7            return INT_MAX
8
9        sign = -1 if (dividend < 0) ^ (divisor < 0) else 1
10
11        dividend = abs(dividend)
12        divisor = abs(divisor)
13
14        result = 0
15
16        while dividend >= divisor:
17            temp = divisor
18            multiple = 1
19
20            while dividend >= (temp << 1):
21                temp <<= 1
22                multiple <<= 1
23
24            dividend -= temp
25            result += multiple
26
27        return sign * result