# Last updated: 7/9/2026, 10:09:42 AM
class Solution:
    def checkStraightLine(self, coordinates):
        x1, y1 = coordinates[0]
        x2, y2 = coordinates[1]

        for x3, y3 in coordinates[2:]:
            if (x2 - x1) * (y3 - y1) != (y2 - y1) * (x3 - x1):
                return False

        return True