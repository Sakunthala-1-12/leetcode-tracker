# Last updated: 7/27/2026, 2:53:16 PM
1class Solution(object):
2    def groupAnagrams(self, strs):
3        groups = defaultdict(list)
4
5        for s in strs:
6            key = "".join(sorted(s))
7            groups[key].append(s)
8
9        return list(groups.values())
10        