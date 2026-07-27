# Last updated: 7/27/2026, 3:14:37 PM
1class Solution(object):
2    def minWindow(self, s, t):
3        if not s or not t:
4            return ""
5
6        need = Counter(t)
7        missing = len(t)
8        left = start = end = 0
9
10        for right, ch in enumerate(s, 1):
11            if need[ch] > 0:
12                missing -= 1
13            need[ch] -= 1
14
15            if missing == 0:
16                while left < right and need[s[left]] < 0:
17                    need[s[left]] += 1
18                    left += 1
19
20                if end == 0 or right - left < end - start:
21                    start, end = left, right
22
23                need[s[left]] += 1
24                missing += 1
25                left += 1
26
27        return s[start:end]