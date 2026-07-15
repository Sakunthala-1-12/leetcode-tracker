# Last updated: 7/15/2026, 9:28:58 AM
1class Solution(object):
2    def fib(self, n):
3        if n == 0:
4            return 0
5
6        if n == 1:
7            return 1
8
9        a = 0
10        b = 1
11
12        for i in range(2, n + 1):
13            c = a + b
14            a = b
15            b = c
16
17        return b
18        