# Last updated: 7/9/2026, 10:11:20 AM
class Solution:
    def postorderTraversal(self, root):
        result = []

        def postorder(node):
            if not node:
                return

            postorder(node.left)
            postorder(node.right)
            result.append(node.val)

        postorder(root)
        return result      