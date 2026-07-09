# Last updated: 7/9/2026, 10:11:42 AM
class Solution:
    def isValidBST(self, root):
        def validate(node, low, high):
            if not node:
                return True

            if node.val <= low or node.val >= high:
                return False

            return (validate(node.left, low, node.val) and
                    validate(node.right, node.val, high))

        return validate(root, float('-inf'), float('inf'))