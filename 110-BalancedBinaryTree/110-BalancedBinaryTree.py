# Last updated: 7/9/2026, 10:11:29 AM
class Solution:
    def isBalanced(self, root):
        def height(node):
            if not node:
                return 0

            left = height(node.left)
            right = height(node.right)

            if left == -1 or right == -1 or abs(left - right) > 1:
                return -1

            return 1 + max(left, right)

        return height(root) != -1