import heapq

class Solution:
    def assignTasks(self, servers: list[int], tasks: list[int]) -> list[int]:
        available = []
        busy = []
        ans = []

        for idx, weight in enumerate(servers):
            heapq.heappush(available, (weight, idx))

        time = 0

        for i, duration in enumerate(tasks):
            time = max(i, time)

            while busy and busy[0][0] <= time:
                finish, weight, idx = heapq.heappop(busy)
                heapq.heappush(available, (weight, idx))

            if not available:
                time = busy[0][0]

                while busy and busy[0][0] <= time:
                    finish, weight, idx = heapq.heappop(busy)
                    heapq.heappush(available, (weight, idx))

            weight, idx = heapq.heappop(available)
            ans.append(idx)

            heapq.heappush(busy, (time + tasks[i], weight, idx))

        return ans