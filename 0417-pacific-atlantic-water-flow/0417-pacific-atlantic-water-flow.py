class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        m, n = len(heights), len(heights[0])
        pacific = set()
        atlantic = set()

        def dfs(r, c, visited):
            visited.add((r, c))

            for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                nr, nc = r + dr, c + dc

                if 0 <= nr < m and 0 <= nc < n and (nr, nc) not in visited and heights[nr][nc] >= heights[r][c]:
                    dfs(nr, nc, visited)

        for c in range(n):
            dfs(0, c, pacific)

        for r in range(m):
            dfs(r, 0, pacific)

        for c in range(n):
            dfs(m - 1, c, atlantic)

        for r in range(m):
            dfs(r, n - 1, atlantic)

        ans = []

        for r in range(m):
            for c in range(n):
                if (r, c) in pacific and (r, c) in atlantic:
                    ans.append([r, c])

        return ans