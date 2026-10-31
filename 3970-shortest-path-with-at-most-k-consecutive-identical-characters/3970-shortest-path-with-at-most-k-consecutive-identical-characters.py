from collections import defaultdict
import heapq

class Solution:
    def shortestPath(self, n: int, edges: List[List[int]], labels: str, k: int) -> int:
        graph = defaultdict(list)

        for u, v, w in edges:
            graph[u].append((v, w))

        dist = {}
        heap = [(0, 0, 1)]

        while heap:
            d, node, count = heapq.heappop(heap)

            if (node, count) in dist:
                continue

            dist[(node, count)] = d

            if node == n - 1:
                return d

            for nei, w in graph[node]:
                if labels[nei] == labels[node]:
                    new_count = count + 1
                else:
                    new_count = 1

                if new_count > k:
                    continue

                if (nei, new_count) not in dist:
                    heapq.heappush(heap, (d + w, nei, new_count))

        return -1