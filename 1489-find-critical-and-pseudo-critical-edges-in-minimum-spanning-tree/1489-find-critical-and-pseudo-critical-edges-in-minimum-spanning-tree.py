class Solution:
    def findCriticalAndPseudoCriticalEdges(self, n: int, edges: list[list[int]]) -> list[list[int]]:
        edges = [(w, u, v, i) for i, (u, v, w) in enumerate(edges)]
        edges.sort()

        def kruskal(skip = -1, force = -1):
            parent = list(range(n))
            size = [1] * n

            def find(x):
                if parent[x] != x:
                    parent[x] = find(parent[x])
                
                return parent[x]

            def union(x, y):
                root_x, root_y = find(x), find(y)

                if root_x == root_y:
                    return False

                if size[root_x] < size[root_y]:
                    root_x, root_y = root_y, root_x

                parent[root_y] = root_x
                size[root_x] += size[root_y]

                return True

            total = count = 0

            if force != -1:
                w, u, v, _ = edges[force]
                
                if union(u, v):
                    count += 1
                    total += w

            for i, (w, u, v, _) in enumerate(edges):
                if i == skip or i == force:
                    continue

                if union(u, v):
                    count += 1
                    total += w

                if count == n - 1:
                    break
            
            if count != n - 1:
                return float("inf")

            return total

        base = kruskal()
        critical = []
        pseudo = []

        for i, (w, u, v, ori_idx) in enumerate(edges):
            if kruskal(skip = i) > base:
                critical.append(ori_idx)
            elif kruskal(force = i) == base:
                pseudo.append(ori_idx)

        return [critical, pseudo]