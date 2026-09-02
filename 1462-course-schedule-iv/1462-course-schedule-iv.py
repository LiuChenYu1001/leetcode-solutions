class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        n = numCourses
        reachable = [[False] * n for _ in range(n)]

        for a, b in prerequisites:
            reachable[a][b] = True

        for k in range(n):
            for i in range(n):
                for j in range(n):
                    if reachable[i][k] and reachable[k][j]:
                        reachable[i][j] = True

        return [reachable[a][b] for a, b in queries]