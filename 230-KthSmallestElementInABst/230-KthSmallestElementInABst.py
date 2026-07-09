# Last updated: 7/9/2026, 10:10:35 AM
class Solution:
    def kthSmallest(self, root, k):
        stack = []

        while True:
            while root:
                stack.append(root)
                root = root.left

            root = stack.pop()
            k -= 1

            if k == 0:
                return root.val

            root = root.right