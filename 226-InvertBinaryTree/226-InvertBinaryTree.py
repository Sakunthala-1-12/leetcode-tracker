# Last updated: 7/9/2026, 10:10:36 AM
class Solution:
    def invertTree(self, root):
        if root:
            root.left, root.right = root.right, root.left
            self.invertTree(root.left)
            self.invertTree(root.right)

        return root