# Last updated: 7/9/2026, 10:11:22 AM
class Solution:
    def preorderTraversal(self, root):
        result = []

        def preorder(node):
            if not node:
                return

            result.append(node.val)
            preorder(node.left)
            preorder(node.right)

        preorder(root)
        return result    