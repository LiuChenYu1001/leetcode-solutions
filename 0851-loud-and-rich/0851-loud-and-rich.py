class Solution:
    def loudAndRich(self, richer: list[list[int]], quiet: list[int]) -> list[int]:
        n = len(quiet)
        graph = [[] for _ in range(n)]

        for a, b in richer:
            graph[b].append(a)

        answer = [-1] * n

        def dfs(i):
            if answer[i] != -1:
                return answer[i]

            answer[i] = i

            for nei in graph[i]:
                candidate = dfs(nei)

                if quiet[candidate] < quiet[answer[i]]:
                    answer[i] = candidate

            return answer[i]

        for i in range(n):
            answer[i] = dfs(i)

        return answer