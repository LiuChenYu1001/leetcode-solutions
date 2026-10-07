import heapq

class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: list[int], capital: list[int]) -> int:
        project = sorted(zip(capital, profits))
        heap = []
        i = 0
        n = len(project)

        for _ in range(k):
            while i < n and project[i][0] <= w:
                profit = project[i][1]
                heapq,heappush(heap, -profit)
                i += 1

            if not heap:
                break

            w += -heapq.heappop(heap)

        return w