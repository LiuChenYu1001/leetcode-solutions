class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = [[] for _ in range(n)]
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        visited = [False] * n
        ans = 0

        for start in range(n):
            if visited[start]:
                continue

            stack = [start]
            visited[start] = True
            node_count = 0
            degree = 0

            while stack:
                node = stack.pop()
                node_count += 1
                degree += len(graph[node])

                for nei in graph[node]:
                    if not visited[nei]:
                        visited[nei] = True
                        stack.append(nei)

            edge_count = degree // 2
            if edge_count == node_count * (node_count - 1) // 2:
                ans += 1

        return ans