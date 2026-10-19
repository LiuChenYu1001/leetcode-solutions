from collections import defaultdict
import heapq

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        graph = defaultdict(list)

        for u, v, price in flights:
            graph[u].append((v, price))

        dist = [[float("inf")] * (k + 2) for _ in range(n)]
        remain = k + 1
        dist[src][remain] = 0
        heap = [(0, src, remain)]

        while heap:
            cost, city, remain = heapq.heappop(heap)

            if city == dst:
                return cost

            if cost > dist[city][remain]:
                continue

            if remain == 0:
                continue
            
            for nei, price in graph[city]:
                new_cost = cost + price
                new_remain = remain - 1

                if new_cost < dist[nei][new_remain]:
                    dist[nei][new_remain] = new_cost
                    heapq.heappush(heap, (new_cost, nei, new_remain))

        return -1

        # 二維 Dijkstra