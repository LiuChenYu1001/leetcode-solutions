from collections import defaultdict
import heapq

class Solution:
    def shortestPath(self, n: int, edges: List[List[int]], labels: str, k: int) -> int:
        graph = defaultdict(list)

        for u, v, w in edges:
            graph[u].append((v, w))

        dist = [[float("inf")] * (k + 1) for _ in range(n)]
        dist[0][1] = 0
        heap = [(0, 0, 1)]

        while heap:
            d, node, count = heapq.heappop(heap)

            if d > dist[node][count]:
                continue

            if node == n - 1:
                return d

            for nei, w in graph[node]:
                if labels[nei] == labels[node]:
                    new_count = count + 1
                else:
                    new_count = 1

                if new_count > k:
                    continue

                new_dist = d + w

                if new_dist < dist[nei][new_count]:
                    dist[nei][new_count] = new_dist
                    heapq.heappush(heap, (new_dist, nei, new_count))

        return -1