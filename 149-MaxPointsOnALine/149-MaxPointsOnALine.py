# Last updated: 7/9/2026, 10:11:18 AM
from collections import defaultdict

class Solution:
    def maxPoints(self, points):
        if len(points) <= 2:
            return len(points)

        ans = 0

        for i in range(len(points)):
            slopes = defaultdict(int)

            for j in range(i + 1, len(points)):
                x1, y1 = points[i]
                x2, y2 = points[j]

                if x1 == x2:
                    slope = "inf"
                else:
                    slope = float(y2 - y1) / (x2 - x1)

                slopes[slope] += 1

            if slopes:
                ans = max(ans, max(slopes.values()) + 1)
            else:
                ans = max(ans, 1)

        return ans