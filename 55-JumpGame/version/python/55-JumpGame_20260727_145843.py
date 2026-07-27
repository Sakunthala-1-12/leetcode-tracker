# Last updated: 7/27/2026, 2:58:43 PM
1class Solution(object):
2    def lengthOfLastWord(self, s):
3        i = len(s) - 1
4
5        while i >= 0 and s[i] == " ":
6            i -= 1
7
8        length = 0
9        while i >= 0 and s[i] != " ":
10            length += 1
11            i -= 1
12
13        return length
14        