from collections import deque
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows, cols = len(grid), len(grid[0])
        count = 0

        def bfs(r, c):
            queue = deque()
            queue.append((r, c))

            grid[r][c] = "0"

            while queue:
                x, y = queue.popleft()

                for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                    nx = x + dx
                    ny = y + dy

                    if 0 <= nx < rows and 0 <= ny < cols and grid[nx][ny] == "1":
                        queue.append((nx, ny))
                        grid[nx][ny] = "0"

            return

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1":
                    bfs(r, c)
                    count += 1

        return count