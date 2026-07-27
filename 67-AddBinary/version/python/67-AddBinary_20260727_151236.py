# Last updated: 7/27/2026, 3:12:36 PM
1class Solution(object):
2    def setZeroes(self, matrix):
3        rows = set()
4        cols = set()
5
6        for i in range(len(matrix)):
7            for j in range(len(matrix[0])):
8                if matrix[i][j] == 0:
9                    rows.add(i)
10                    cols.add(j)
11
12        for i in range(len(matrix)):
13            for j in range(len(matrix[0])):
14                if i in rows or j in cols:
15                    matrix[i][j] = 0