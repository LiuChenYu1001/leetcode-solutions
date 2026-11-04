class Solution:
    def maximalRectangle(self, matrix: list[list[str]]) -> int:
        m, n = len(matrix), len(matrix[0])
        new_matrix = [[0] * n for _ in range(m)]

        for i in range(m):
            for j in range(n):
                if matrix[i][j] == "1":
                    if i == 0:
                        new_matrix[i][j] = 1
                    else:
                        new_matrix[i][j] = new_matrix[i - 1][j] + 1

        ans = 0

        for r in range(m):
            stack = []

            for c in range(n):
                while stack and new_matrix[r][stack[-1]] > new_matrix[r][c]:
                    h = new_matrix[r][stack.pop()]

                    if not stack:
                        w = c
                    else:
                        w = c - stack[-1] - 1

                    ans = max(ans, h * w)

                stack.append(c)

            while stack:
                h = new_matrix[r][stack.pop()]

                if not stack:
                    w = n
                else:
                    w = n - stack[-1] - 1

                ans = max(ans, h * w)

        return ans