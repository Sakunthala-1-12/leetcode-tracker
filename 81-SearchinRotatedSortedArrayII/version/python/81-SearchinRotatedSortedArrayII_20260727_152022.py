# Last updated: 7/27/2026, 3:20:22 PM
1class Solution(object):
2    def largestRectangleArea(self, heights):
3        stack = []
4        max_area = 0
5        heights.append(0)
6
7        for i in range(len(heights)):
8            while stack and heights[stack[-1]] > heights[i]:
9                h = heights[stack.pop()]
10                w = i if not stack else i - stack[-1] - 1
11                max_area = max(max_area, h * w)
12            stack.append(i)
13
14        return max_area