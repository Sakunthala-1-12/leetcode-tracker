# Last updated: 7/27/2026, 2:58:27 PM
1class Solution(object):
2    def insert(self, intervals, newInterval):
3        result = []
4        i = 0
5        n = len(intervals)
6
7        while i < n and intervals[i][1] < newInterval[0]:
8            result.append(intervals[i])
9            i += 1
10
11        while i < n and intervals[i][0] <= newInterval[1]:
12            newInterval[0] = min(newInterval[0], intervals[i][0])
13            newInterval[1] = max(newInterval[1], intervals[i][1])
14            i += 1
15
16        result.append(newInterval)
17
18        while i < n:
19            result.append(intervals[i])
20            i += 1
21
22        return result