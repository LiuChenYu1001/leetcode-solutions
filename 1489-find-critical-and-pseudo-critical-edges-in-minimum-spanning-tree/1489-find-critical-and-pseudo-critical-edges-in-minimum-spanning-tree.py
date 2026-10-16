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

            def union(a, b):
                ra, rb = find(a), find(b)

                if ra == rb:
                    return False

                if size[ra] < size[rb]:
                    ra, rb = rb, ra

                parent[rb] = ra
                size[ra] += size[rb]

                return True

            total = count = 0

            if force != -1:
                w, u, v, _ = edges[force]
                if union(u, v):
                    total += w
                    count += 1

            for i, (w, u, v, _) in enumerate(edges):
                if i == skip or i == force:
                    continue

                if union(u, v):
                    total += w
                    count += 1

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