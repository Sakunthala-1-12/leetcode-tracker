# Last updated: 7/27/2026, 3:10:41 PM
1class Solution(object):
2    def fullJustify(self, words, maxWidth):
3        result = []
4        i = 0
5
6        while i < len(words):
7            line_len = len(words[i])
8            j = i + 1
9
10            while j < len(words) and line_len + 1 + len(words[j]) <= maxWidth:
11                line_len += 1 + len(words[j])
12                j += 1
13
14            line_words = words[i:j]
15            spaces = maxWidth - sum(len(w) for w in line_words)
16
17            if j == len(words) or len(line_words) == 1:
18                line = " ".join(line_words)
19                line += " " * (maxWidth - len(line))
20            else:
21                gaps = len(line_words) - 1
22                even = spaces // gaps
23                extra = spaces % gaps
24
25                line = ""
26                for k in range(gaps):
27                    line += line_words[k]
28                    line += " " * (even + (1 if k < extra else 0))
29                line += line_words[-1]
30
31            result.append(line)
32            i = j
33
34        return result
35        