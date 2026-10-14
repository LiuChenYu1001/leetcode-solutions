import heapq

class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        m, n = len(heights), len(heights[0])

        heap = [(0, 0, 0)]
        effort = [[float("inf")] * n for _ in range(m)]
        effort[0][0] = 0
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        while heap:
            curr_effort, r, c = heapq.heappop(heap)

            if (r, c) == (m - 1, n - 1):
                return curr_effort

            for dr, dc in directions:
                nr, nc = r + dr, c + dc

                if not (0 <= nr < m and 0 <= nc < n):
                    continue

                diff = abs(heights[nr][nc] - heights[r][c])
                new_effort = max(curr_effort, diff)

                if new_effort < effort[nr][nc]:
                    effort[nr][nc] = new_effort
                    heapq.heappush(heap, (new_effort, nr, nc))

        return effort[m - 1][n - 1] 