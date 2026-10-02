# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import deque

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        if not root:
            return ""

        res = []
        q = deque([root])

        while q:
            node = q.popleft()

            if node:
                res.append(str(node.val))
                q.append(node.left)
                q.append(node.right)
            else:
                res.append("#")

        return ",".join(res)

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if not data:
            return None

        vals = data.split(",")
        root = TreeNode(int(vals[0]))
        q = deque([root])
        idx = 1

        while q:
            node = q.popleft()

            if vals[idx] != "#":
                node.left = TreeNode(int(vals[idx]))
                q.append(node.left)
            idx += 1

            if vals[idx] != "#":
                node.right = TreeNode(int(vals[idx]))
                q.append(node.right)
            idx += 1

        return root

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))