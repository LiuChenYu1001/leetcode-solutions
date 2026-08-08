class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        row = len(grid)
        col = len(grid[0])
        ans = 0

        for r in range(row):
            for c in range(col):
                if grid[r][c] == 1:
                    ans += 4

                    if r > 0 and grid[r - 1][c] == 1:
                        ans -= 2

                    if c > 0 and grid[r][c - 1] == 1:
                        ans -= 2

        return ans