# Last updated: 7/27/2026, 3:00:31 PM
1class Solution(object):
2    def generateMatrix(self, n):
3        matrix = [[0] * n for _ in range(n)]
4
5        left, right = 0, n - 1
6        top, bottom = 0, n - 1
7        num = 1
8
9        while left <= right and top <= bottom:
10            for i in range(left, right + 1):
11                matrix[top][i] = num
12                num += 1
13            top += 1
14
15            for i in range(top, bottom + 1):
16                matrix[i][right] = num
17                num += 1
18            right -= 1
19
20            for i in range(right, left - 1, -1):
21                matrix[bottom][i] = num
22                num += 1
23            bottom -= 1
24
25            for i in range(bottom, top - 1, -1):
26                matrix[i][left] = num
27                num += 1
28            left += 1
29
30        return matrix
31        