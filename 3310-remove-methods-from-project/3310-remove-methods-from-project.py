from collections import defaultdict
class Solution:
    def remainingMethods(self, n: int, k: int, invocations: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        for v, r in invocations:
            graph[v].append(r)

        suspicious = [False] * n
        suspicious[k] = True

        def dfs(node):
            suspicious[node] = True

            for nei in graph[node]:
                if not suspicious[nei]:
                    dfs(nei)

        dfs(k)

        for v, r in invocations:
            if not suspicious[v] and suspicious[r]:
                return list(range(n))

        ans = []

        for i in range(n):
            if not suspicious[i]:
                ans.append(i)

        return ans