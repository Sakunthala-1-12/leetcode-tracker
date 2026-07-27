# Last updated: 7/27/2026, 3:15:56 PM
1class Solution(object):
2    def exist(self, board, word):
3        rows = len(board)
4        cols = len(board[0])
5
6        def dfs(r, c, index):
7            if index == len(word):
8                return True
9
10            if (
11                r < 0 or r >= rows or
12                c < 0 or c >= cols or
13                board[r][c] != word[index]
14            ):
15                return False
16
17            temp = board[r][c]
18            board[r][c] = "#"
19
20            found = (
21                dfs(r + 1, c, index + 1) or
22                dfs(r - 1, c, index + 1) or
23                dfs(r, c + 1, index + 1) or
24                dfs(r, c - 1, index + 1)
25            )
26
27            board[r][c] = temp
28            return found
29
30        for r in range(rows):
31            for c in range(cols):
32                if dfs(r, c, 0):
33                    return True
34
35        return False