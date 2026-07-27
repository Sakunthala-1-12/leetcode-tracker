# Last updated: 7/27/2026, 3:04:26 PM
1class Solution(object):
2    def getPermutation(self, n, k):
3        numbers = [str(i) for i in range(1, n + 1)]
4        factorial = [1] * n
5
6        for i in range(1, n):
7            factorial[i] = factorial[i - 1] * i
8
9        k -= 1
10        result = ""
11
12        for i in range(n, 0, -1):
13            index = k // factorial[i - 1]
14            result += numbers.pop(index)
15            k %= factorial[i - 1]
16
17        return result
18        