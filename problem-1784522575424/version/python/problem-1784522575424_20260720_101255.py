# Last updated: 7/20/2026, 10:12:55 AM
1class Solution(object):
2    def multiply(self, num1, num2):
3        if num1 == "0" or num2 == "0":
4            return "0"
5
6        m = len(num1)
7        n = len(num2)
8        result = [0] * (m + n)
9
10        for i in range(m - 1, -1, -1):
11            for j in range(n - 1, -1, -1):
12                mul = (ord(num1[i]) - ord('0')) * (ord(num2[j]) - ord('0'))
13                total = mul + result[i + j + 1]
14
15                result[i + j + 1] = total % 10
16                result[i + j] += total // 10
17
18        answer = ""
19
20        for digit in result:
21            if not (answer == "" and digit == 0):
22                answer += str(digit)
23
24        return answer
25        