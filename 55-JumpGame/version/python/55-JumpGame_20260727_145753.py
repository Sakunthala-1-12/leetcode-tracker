# Last updated: 7/27/2026, 2:57:53 PM
1class Solution(object):
2    def merge(self, intervals):
3        intervals.sort()
4        result = []
5
6        for interval in intervals:
7            if not result or result[-1][1] < interval[0]:
8                result.append(interval)
9            else:
10                result[-1][1] = max(result[-1][1], interval[1])
11
12        return result
13        