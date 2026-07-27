# Last updated: 7/27/2026, 2:55:32 PM
1class Solution(object):
2    def totalNQueens(self, n):
3        cols = set()
4        diag1 = set()   # row - col
5        diag2 = set()   # row + col
6
7        def backtrack(row):
8            if row == n:
9                return 1
10
11            count = 0
12            for col in range(n):
13                if col in cols or (row - col) in diag1 or (row + col) in diag2:
14                    continue
15
16                cols.add(col)
17                diag1.add(row - col)
18                diag2.add(row + col)
19
20                count += backtrack(row + 1)
21
22                cols.remove(col)
23                diag1.remove(row - col)
24                diag2.remove(row + col)
25
26            return count
27
28        return backtrack(0)
29        