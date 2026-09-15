class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        m, n = len(matrix), len(matrix[0])
        dp = [[0] * n for _ in range(m)]
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        def dfs(r, c):
            if dp[r][c] != 0:
                return dp[r][c]

            ans = 1

            for dr, dc in directions:
                nr, nc = r + dr, c + dc

                if 0 <= nr < m and 0 <= nc < n and matrix[r][c] < matrix[nr][nc]:
                    ans = max(ans, 1 + dfs(nr, nc))

            dp[r][c] = ans

            return ans

        ans = 0

        for r in range(m):
            for c in range(n):
                ans = max(ans, dfs(r, c))

        return ans