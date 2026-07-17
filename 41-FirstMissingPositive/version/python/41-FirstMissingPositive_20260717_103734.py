# Last updated: 7/17/2026, 10:37:34 AM
1class Solution(object):
2    def trap(self, height):
3        left = 0
4        right = len(height) - 1
5        left_max = 0
6        right_max = 0
7        water = 0
8
9        while left < right:
10            if height[left] < height[right]:
11                if height[left] >= left_max:
12                    left_max = height[left]
13                else:
14                    water += left_max - height[left]
15                left += 1
16            else:
17                if height[right] >= right_max:
18                    right_max = height[right]
19                else:
20                    water += right_max - height[right]
21                right -= 1
22
23        return water
24        