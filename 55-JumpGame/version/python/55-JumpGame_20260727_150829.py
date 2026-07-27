# Last updated: 7/27/2026, 3:08:29 PM
1class Solution(object):
2    def isNumber(self, s):
3        s = s.strip()
4
5        seen_digit = False
6        seen_dot = False
7        seen_exp = False
8
9        for i, ch in enumerate(s):
10            if ch.isdigit():
11                seen_digit = True
12            elif ch in ['+', '-']:
13                if i > 0 and s[i - 1].lower() != 'e':
14                    return False
15            elif ch == '.':
16                if seen_dot or seen_exp:
17                    return False
18                seen_dot = True
19            elif ch.lower() == 'e':
20                if seen_exp or not seen_digit:
21                    return False
22                seen_exp = True
23                seen_digit = False
24            else:
25                return False
26
27        return seen_digit
28        