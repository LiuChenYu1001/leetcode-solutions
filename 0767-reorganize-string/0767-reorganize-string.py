from collections import Counter
import heapq

class Solution:
    def reorganizeString(self, s: str) -> str:
        count = Counter(s)
        heap = [(-freq, ch) for ch, freq in count.items()]
        heapq.heapify(heap)

        ans = []
        pre_ch = ""
        pre_count = 0

        while heap:
            count, ch = heapq.heappop(heap)
            ans.append(ch)
            count += 1

            if pre_count < 0:
                heapq.heappush(heap, (pre_count, pre_ch))

            pre_count = count
            pre_ch = ch

        if pre_count < 0:
            return ""

        return "".join(ans)