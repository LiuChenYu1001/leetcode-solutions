from collections import defaultdict
import heapq

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        graph = defaultdict(list)

        for u, v, price in flights:
            graph[u].append((v, price))

        dist = {}
        heap = [(0, src, k + 1)]

        while heap:
            cost, city, remain = heapq.heappop(heap)

            if (city, remain) in dist:
                continue

            dist[(city, remain)] = cost

            if city == dst:
                return cost

            if remain == 0:
                continue
            
            for nei, price in graph[city]:
                if (nei, remain - 1) not in dist:
                    heapq.heappush(heap, (cost + price, nei, remain - 1))

        return -1

        # 二維 Dijkstra