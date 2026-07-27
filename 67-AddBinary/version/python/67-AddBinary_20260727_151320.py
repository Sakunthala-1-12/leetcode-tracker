# Last updated: 7/27/2026, 3:13:20 PM
1class Solution(object):
2    def searchMatrix(self, matrix, target):
3        if not matrix or not matrix[0]:
4            return False
5
6        m, n = len(matrix), len(matrix[0])
7        left, right = 0, m * n - 1
8
9        while left <= right:
10            mid = (left + right) // 2
11            value = matrix[mid // n][mid % n]
12
13            if value == target:
14                return True
15            elif value < target:
16                left = mid + 1
17            else:
18                right = mid - 1
19
20        return False
21        