import heapq

class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        heap = []

        if a:
            heapq.heappush(heap, (-a, "a"))
        if b:
            heapq.heappush(heap, (-b, "b"))
        if c:
            heapq.heappush(heap, (-c, "c"))

        ans = []

        while heap:
            count_1, ch_1 = heapq.heappop(heap)

            if len(ans) >= 2 and ans[-1] == ch_1 and ans[-2] == ch_1:
                if not heap:
                    break
                
                count_2, ch_2 = heapq.heappop(heap)
                ans.append(ch_2)
                count_2 += 1

                if count_2 < 0:
                    heapq.heappush(heap, (count_2, ch_2))

                heapq.heappush(heap, (count_1, ch_1))

            else:
                ans.append(ch_1)
                count_1 += 1

                if count_1 < 0:
                    heapq.heappush(heap, (count_1, ch_1))

        return "".join(ans)