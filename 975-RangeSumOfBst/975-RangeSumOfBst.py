# Last updated: 7/9/2026, 10:09:45 AM
class Solution:
    def rangeSumBST(self, root, low, high):
        if not root:
            return 0

        if root.val < low:
            return self.rangeSumBST(root.right, low, high)

        if root.val > high:
            return self.rangeSumBST(root.left, low, high)

        return (root.val +
                self.rangeSumBST(root.left, low, high) +
                self.rangeSumBST(root.right, low, high))     