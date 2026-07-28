# Last updated: 7/28/2026, 3:05:43 PM
1class Solution(object):
2    def smallestPalindrome(self, s):
3        count = Counter(s)
4
5        left = []
6        middle = ""
7
8        for ch in sorted(count.keys()):
9            left.append(ch * (count[ch] // 2))
10            if count[ch] % 2:
11                middle = ch
12
13        left = "".join(left)
14        return left + middle + left[::-1]
15        