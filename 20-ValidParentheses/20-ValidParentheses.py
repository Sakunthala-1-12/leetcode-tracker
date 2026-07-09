# Last updated: 7/9/2026, 10:12:08 AM
class Solution:
    def isValid(self, s):
        stack = []
        mp = {')': '(', '}': '{', ']': '['}

        for ch in s:
            if ch in mp:
                if not stack or stack.pop() != mp[ch]:
                    return False
            else:
                stack.append(ch)

        return len(stack) == 0    