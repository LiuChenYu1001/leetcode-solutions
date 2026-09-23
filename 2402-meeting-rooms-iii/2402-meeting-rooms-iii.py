import heapq

class Solution:
    def mostBooked(self, n: int, meetings: list[list[int]]) -> int:
        meetings.sort()
        available = list(range(n))
        heapq.heapify(available)
        used = []
        count = [0] * n

        for start, end in meetings:
            while used and used[0][0] <= start:
                end_time, room = heapq.heappop(used)
                heapq.heappush(available, room)

            duration = end - start

            if available:
                room = heapq.heappop(available)
                heapq.heappush(used, (end, room))

            else:
                end_time, room = heapq.heappop(used)
                new_end = end_time + duration
                heapq.heappush(used, (new_end, room))

            count[room] += 1

        ans = 0

        for room in range(1, n):
            if count[room] > count[ans]:
                ans = room

        return ans      