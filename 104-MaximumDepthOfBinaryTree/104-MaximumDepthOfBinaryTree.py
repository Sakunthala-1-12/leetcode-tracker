# Last updated: 7/9/2026, 10:11:33 AM
class Solution:
    def maxDepth(self, root):
        if not root:
            return 0

        return 1 + max(self.maxDepth(root.left),
                       self.maxDepth(root.right))      