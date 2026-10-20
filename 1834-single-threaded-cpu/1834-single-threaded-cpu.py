import heapq

class Solution:
    def getOrder(self, tasks: list[list[int]]) -> list[int]:
        tasks = sorted((enque, process, idx) for idx, (enque, process) in enumerate(tasks))
        i = time = 0
        n = len(tasks)
        heap = []
        ans = []

        while i < n or heap:
            if not heap and i < n:
                time = max(time, tasks[i][0])

            while i < n and tasks[i][0] <= time:
                enque, process, idx = tasks[i]
                heapq.heappush(heap, (process, idx))
                i += 1

            process, idx = heapq.heappop(heap)
            ans.append(idx)
            time += process

        return ans