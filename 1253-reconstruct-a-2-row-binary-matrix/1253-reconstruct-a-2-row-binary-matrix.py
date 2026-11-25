class Solution:
    def reconstructMatrix(self, upper: int, lower: int, colsum: list[int]) -> list[list[int]]:
        n = len(colsum)
        ans = [[0] * n for _ in range(2)]

        if upper + lower != sum(colsum):
            return []

        for j in range(n):
            if colsum[j] == 2:
                ans[0][j] = 1
                ans[1][j] = 1
                upper -= 1
                lower -= 1

        if upper < 0 or lower < 0:
            return []

        for j in range(n):
            if colsum[j] == 1:
                if upper > 0:
                    ans[0][j] = 1
                    upper -= 1
                else:
                    ans[1][j] = 1
                    lower -= 1

        if upper != 0 or lower != 0:
            return []

        return ans