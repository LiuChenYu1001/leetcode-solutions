import heapq

class Solution:
    def minInterval(self, intervals: list[list[int]], queries: list[int]) -> list[int]:
        intervals.sort()
        heap = []
        idx = 0
        ans = {}

        for q in sorted(queries):
            while idx < len(intervals) and intervals[idx][0] <= q:
                left, right = intervals[idx]
                length = right - left + 1
                heapq.heappush(heap, (length, right))
                idx += 1

            while heap and heap[0][1] < q:
                heapq.heappop(heap)

            if heap:
                ans[q] = heap[0][0]
            else:
                ans[q] = -1

        return [ans[q] for q in queries]