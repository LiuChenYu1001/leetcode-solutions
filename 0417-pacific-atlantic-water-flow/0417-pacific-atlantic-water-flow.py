class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        m, n = len(heights), len(heights[0])
        pacific = set()
        atlantic = set()

        def bfs(r, c, visited):
            q = deque([(r, c)])
            visited.add((r, c))

            while q:
                r, c = q.popleft()

                for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                    nr, nc = r + dr, c + dc

                    if (
                        0 <= nr < m
                        and 0 <= nc < n
                        and (nr, nc) not in visited
                        and heights[nr][nc] >= heights[r][c]
                    ):
                        visited.add((nr, nc))
                        q.append((nr, nc))

        for c in range(n):
            bfs(0, c, pacific)

        for r in range(m):
            bfs(r, 0, pacific)

        for c in range(n):
            bfs(m - 1, c, atlantic)

        for r in range(m):
            bfs(r, n - 1, atlantic)

        ans = []

        for r in range(m):
            for c in range(n):
                if (r, c) in pacific and (r, c) in atlantic:
                    ans.append([r, c])

        return ans