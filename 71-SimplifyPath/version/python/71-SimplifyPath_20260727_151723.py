# Last updated: 7/27/2026, 3:17:23 PM
1class Solution(object):
2    def simplifyPath(self, path):
3        stack = []
4
5        for part in path.split("/"):
6            if part == "" or part == ".":
7                continue
8            elif part == "..":
9                if stack:
10                    stack.pop()
11            else:
12                stack.append(part)
13
14        return "/" + "/".join(stack)