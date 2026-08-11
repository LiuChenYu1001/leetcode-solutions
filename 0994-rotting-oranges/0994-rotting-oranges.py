from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        row, col = len(grid), len(grid[0])
        visited = [[-1] * col for _ in range(row)]
        queue = deque()

        for r in range(row):
            for c in range(col):
                if grid[r][c] == 2:
                    visited[r][c] = 0
                    queue.append((r, c))

        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        while queue:
            r, c = queue.popleft()

            for dr, dc in directions:
                nr = r + dr
                nc = c + dc

                if 0 <= nr < row and 0 <= nc < col and grid[nr][nc] == 1:
                    grid[nr][nc] = 2
                    visited[nr][nc] = visited[r][c] + 1
                    queue.append((nr, nc))

        ans = 0
        for r in range(row):
            for c in range(col):
                if grid[r][c] == 1:
                    return -1
                if grid[r][c] == 2:
                    ans = max(ans, visited[r][c])

        return ans