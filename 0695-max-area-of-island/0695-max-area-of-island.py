class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        ans = 0

        def dfs(r, c):
            if r < 0 or r >= m or c < 0 or c >= n:
                return 0

            if grid[r][c] != 1:
                return 0

            grid[r][c] = 0
            area = 1

            area += dfs(r - 1, c)
            area += dfs(r + 1,c)
            area += dfs(r,c + 1)
            area += dfs(r,c - 1)

            return area

        for r in range(m):
            for c in range(n):
                if grid[r][c] == 1:
                    ans = max(ans, dfs(r ,c))
        
        return ans