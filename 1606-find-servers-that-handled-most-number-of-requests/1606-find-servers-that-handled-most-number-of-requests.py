import heapq

class Solution:
    def busiestServers(self, k: int, arrival: list[int], load: list[int]) -> list[int]:
        available = list(range(k))
        heapq.heapify(available)
        busy = []
        count = [0] * k

        for i in range(len(arrival)):
            time = arrival[i]

            while busy and busy[0][0] <= time:
                end_time, server = heapq.heappop(busy)
                heapq.heappush(available, (i + (server - i) % k))

            if not available:
                continue

            server = heapq.heappop(available) % k
            count[server] += 1
            heapq.heappush(busy, (load[i] + time, server))

        max_count = max(count)

        return [i for i in range(k) if count[i] == max_count]