# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: TreeNode | None) -> int:
        self.ans = float("-inf")

        def postorder(node):
            if not node:
                return 0

            left_sum = max(postorder(node.left), 0)
            right_sum = max(postorder(node.right), 0)

            self.ans = max(self.ans, left_sum + right_sum + node.val)

            return max(left_sum, right_sum) + node.val

        postorder(root)

        return self.ans