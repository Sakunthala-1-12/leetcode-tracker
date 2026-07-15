# Last updated: 7/15/2026, 3:08:59 PM
1class Solution(object):
2    def findSubstring(self, s, words):
3        if not s or not words:
4            return []
5
6        word_len = len(words[0])
7        word_num = len(words)
8        total_len = word_len * word_num
9        word_count = Counter(words)
10        ans = []
11
12        for i in range(word_len):
13            left = i
14            count = 0
15            seen = {}
16
17            for j in range(i, len(s) - word_len + 1, word_len):
18                word = s[j:j + word_len]
19
20                if word in word_count:
21                    seen[word] = seen.get(word, 0) + 1
22                    count += 1
23
24                    while seen[word] > word_count[word]:
25                        left_word = s[left:left + word_len]
26                        seen[left_word] -= 1
27                        left += word_len
28                        count -= 1
29
30                    if count == word_num:
31                        ans.append(left)
32                        left_word = s[left:left + word_len]
33                        seen[left_word] -= 1
34                        left += word_len
35                        count -= 1
36                else:
37                    seen.clear()
38                    count = 0
39                    left = j + word_len
40
41        return ans