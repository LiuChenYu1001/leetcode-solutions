import heapq
from collections import deque

class Solution:
    def maximumSafenessFactor(self, grid: List[List[int]]) -> int:
        n = len(grid)
        dist = [[-1] * n for _ in range(n)]
        q = deque()

        for r in range(n):
            for c in range(n):
                if grid[r][c] == 1:
                    dist[r][c] = 0
                    q.append((r, c))

        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        while q:
            r, c = q.popleft()

            for dr, dc in directions:
                nr, nc = r + dr, c + dc

                if 0 <= nr < n and 0 <= nc < n and dist[nr][nc] == -1:
                    dist[nr][nc] = dist[r][c] + 1
                    q.append((nr, nc))

        best = [[-1] * n for _ in range(n)]
        best[0][0] = dist[0][0]
        heap = [(-dist[0][0], 0, 0)]

        while heap:
            safe, r, c = heapq.heappop(heap)
            safe = -safe

            if safe < best[r][c]:
                continue

            if (r, c) == (n - 1, n - 1):
                return safe

            for dr, dc in directions:
                nr, nc = r + dr, c + dc

                if 0 <= nr < n and 0 <= nc < n:
                    new_safe = min(safe, dist[nr][nc])

                    if new_safe > best[nr][nc]:
                        best[nr][nc] = new_safe
                        heapq.heappush(heap, (-new_safe, nr, nc)) 

        return 0  