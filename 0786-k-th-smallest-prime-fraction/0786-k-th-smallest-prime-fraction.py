import heapq

class Solution:
    def kthSmallestPrimeFraction(self, arr: list[int], k: int) -> list[int]:
        heap = []
        n = len(arr)

        for i in range(n):
            for j in range(i + 1, n):
                heapq.heappush(heap, (arr[i] / arr[j], arr[i], arr[j]))

        while k > 1:
            heapq.heappop(heap)
            k -= 1

        _, a, b = heapq.heappop(heap)

        return [a, b]