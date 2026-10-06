class Solution:
    def getOrder(self, tasks: list[list[int]]) -> list[int]:
        tasks = sorted((enque, processing, idx) for idx, (enque, processing) in enumerate(tasks))
        heap = []
        ans = []
        i = time = 0
        n = len(tasks)

        while i < n or heap:
            if not heap and i < n:
                time = max(time, tasks[i][0])

            while i < n and tasks[i][0] <= time:
                enque, processing, idx = tasks[i]
                heapq.heappush(heap, (processing, idx))
                i += 1

            processing, idx = heapq.heappop(heap)
            time += processing
            ans.append(idx)

        return ans