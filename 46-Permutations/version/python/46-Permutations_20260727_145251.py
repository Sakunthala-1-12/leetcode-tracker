# Last updated: 7/27/2026, 2:52:51 PM
1class Solution(object):
2    def rotate(self,matrix):
3        n = len(matrix)
4
5        for i in range(n):
6            for j in range(i + 1, n):
7                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
8
9        for row in matrix:
10            row.reverse()
11        