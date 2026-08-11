"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""

class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':
        n = len(grid)

        def build(row, col, size):
            first = grid[row][col]
            is_same = True

            for i in range(row, row + size):
                for j in range(col, col + size):
                    if grid[i][j] != first:
                        is_same = False
                        break
                if not is_same:
                    break

            if is_same:
                return Node(first == 1, True)

            half = size // 2

            return Node(
                True,
                False,
                build(row, col, half),
                build(row, col + half, half),
                build(row + half, col, half),
                build(row + half, col + half, half)
            )

        return build(0, 0, n)