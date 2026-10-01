from collections import Counter
import heapq

class Solution:
    def reorganizeString(self, s: str) -> str:
        count = Counter(s)
        heap = [(-freq, ch) for ch, freq in count.items()]
        heapq.heapify(heap)

        result = []
        prev_count = 0
        prev_ch = ""

        while heap:
            count, ch = heapq.heappop(heap)
            result.append(ch)
            count += 1

            if prev_count < 0:
                heapq.heappush(heap, (prev_count, prev_ch))

            prev_count = count
            prev_ch = ch

        if prev_count < 0:
            return ""

        return "".join(result)