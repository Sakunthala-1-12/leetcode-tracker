# Last updated: 7/27/2026, 2:56:42 PM
1class Solution(object):
2    def spiralOrder(self, matrix):
3        result = []
4
5        if not matrix:
6            return result
7
8        top = 0
9        bottom = len(matrix) - 1
10        left = 0
11        right = len(matrix[0]) - 1
12
13        while top <= bottom and left <= right:
14            for i in range(left, right + 1):
15                result.append(matrix[top][i])
16            top += 1
17
18            for i in range(top, bottom + 1):
19                result.append(matrix[i][right])
20            right -= 1
21
22            if top <= bottom:
23                for i in range(right, left - 1, -1):
24                    result.append(matrix[bottom][i])
25                bottom -= 1
26
27            if left <= right:
28                for i in range(bottom, top - 1, -1):
29                    result.append(matrix[i][left])
30                left += 1
31
32        return result
33        