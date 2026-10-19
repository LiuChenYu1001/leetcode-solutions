import heapq

class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        visited = [False] * n
        heap = [(0, 0)]
        ans = count = 0

        while count < n:
            cost, u = heapq.heappop(heap)

            if visited[u]:
                continue

            visited[u] = True
            ans += cost
            count += 1

            for j in range(n):
                if not visited[j]:
                    new_cost = abs(points[u][0] - points[j][0]) + abs(points[u][1] - points[j][1])
                    heapq.heappush(heap, (new_cost, j))

        return ans

        # Prim + Heap