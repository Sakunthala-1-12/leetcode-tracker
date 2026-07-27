# Last updated: 7/27/2026, 3:20:53 PM
1class Solution(object):
2    def maximalRectangle(self, matrix):
3        if not matrix:
4            return 0
5
6        def largestRectangleArea(heights):
7            stack = []
8            max_area = 0
9            heights.append(0)
10
11            for i in range(len(heights)):
12                while stack and heights[stack[-1]] > heights[i]:
13                    h = heights[stack.pop()]
14                    w = i if not stack else i - stack[-1] - 1
15                    max_area = max(max_area, h * w)
16                stack.append(i)
17
18            heights.pop()
19            return max_area
20
21        cols = len(matrix[0])
22        heights = [0] * cols
23        ans = 0
24
25        for row in matrix:
26            for j in range(cols):
27                if row[j] == "1":
28                    heights[j] += 1
29                else:
30                    heights[j] = 0
31
32            ans = max(ans, largestRectangleArea(heights))
33
34        return ans