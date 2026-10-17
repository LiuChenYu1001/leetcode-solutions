import heapq

class Solution:
    def kthSmallestPrimeFraction(self, arr: list[int], k: int) -> list[int]:
        heap = []
        n = len(arr)

        for i in range(n - 1):
            heapq.heappush(heap, (arr[i] / arr[n - 1], i, n - 1))

        while k > 1:
            _, i, j = heapq.heappop(heap)

            if j - 1 > i:
                heapq.heappush(heap, (arr[i] / arr[j - 1], i, j - 1))

            k -= 1

        _, i, j = heapq.heappop(heap)

        return [arr[i], arr[j]]