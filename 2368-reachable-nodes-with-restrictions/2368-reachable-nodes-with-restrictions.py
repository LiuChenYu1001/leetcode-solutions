from collections import defaultdict

class Solution:
    def reachableNodes(self, n: int, edges: List[List[int]], restricted: List[int]) -> int:
        graph = defaultdict(list)
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)

        restricted = set(restricted)
        visited = set()

        def dfs(node):
            visited.add(node)

            for nei in graph[node]:
                if nei in restricted:
                    continue

                if nei in visited:
                    continue

                dfs(nei)

        dfs(0)

        return len(visited)