import heapq

class Solution:
    def kClosest(self, points: list[list[int]], k: int) -> list[list[int]]:
        heap = []

        for x, y in points:
            dist = x * x + y * y
            heapq.heappush(heap, (dist, x, y))

        ans = []

        for _ in range(k):
            dist, x, y = heapq.heappop(heap)
            ans.append([x, y])

        return ans

        #Min Heap