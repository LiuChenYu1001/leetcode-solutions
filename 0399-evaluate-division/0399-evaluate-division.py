from collections import defaultdict

class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph = defaultdict(list)

        for (a, b), value in zip(equations, values):
            graph[a].append((b, value))
            graph[b].append((a, 1 / value))

        def dfs(curr, target):
            if curr == target:
                return 1.0

            visited.add(curr)

            for nei, weight in graph[curr]:
                if nei not in visited:
                    result = dfs(nei, target)

                    if result != -1.0:
                        return weight * result

            return -1.0

        ans = []
        for start, target in queries:
            if start not in graph or target not in graph:
                ans.append(-1.0)
                continue

            visited = set()
            ans.append(dfs(start, target))

        return ans
