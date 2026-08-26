# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        def dfs(node):
            if not node:
                return (0, 0)

            left_rob, left_not_rob = dfs(node.left)
            right_rob, right_not_rob = dfs(node.right)

            rob_this = node.val + left_not_rob + right_not_rob
            not_rob_this = max(left_rob, left_not_rob) + max(right_rob, right_not_rob)

            return (rob_this, not_rob_this)

        rob_root, not_rob_root = dfs(root)
        
        return max(rob_root, not_rob_root)