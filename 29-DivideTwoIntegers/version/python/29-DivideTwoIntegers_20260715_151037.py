# Last updated: 7/15/2026, 3:10:37 PM
1class Solution(object):
2    def longestValidParentheses(self, s):
3        stack = [-1]
4        max_len = 0
5
6        for i in range(len(s)):
7            if s[i] == '(':
8                stack.append(i)
9            else:
10                stack.pop()
11                if not stack:
12                    stack.append(i)
13                else:
14                    max_len = max(max_len, i - stack[-1])
15
16        return max_len
17        