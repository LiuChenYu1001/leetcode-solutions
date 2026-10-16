from collections import deque

class Solution:
    def buildMatrix(self, k: int, rowConditions: list[list[int]], colConditions: list[list[int]]) -> list[list[int]]:
        def topoSort(conditions):
            graph = [[] for _ in range(k + 1)]
            indegree = [0] * (k + 1)

            for u, v in conditions:
                graph[u].append(v)
                indegree[v] += 1

            q = deque(i for i in range(1, k + 1) if indegree[i] == 0)
            order = []

            while q:
                u = q.popleft()
                order.append(u)

                for nei in graph[u]:
                    indegree[nei] -= 1

                    if indegree[nei] == 0:
                        q.append(nei)

            if len(order) != k:
                return []

            return order

        rowOrder = topoSort(rowConditions)
        colOrder = topoSort(colConditions)

        if not rowOrder or not colOrder:
            return []

        row_pos = {num: i for i, num in enumerate(rowOrder)}
        col_pos = {num: i for i, num in enumerate(colOrder)}

        matrix = [[0] * k for _ in range(k)]

        for num in range(1, k + 1):
            row = row_pos[num]
            col = col_pos[num]
            matrix[row][col] = num

        return matrix