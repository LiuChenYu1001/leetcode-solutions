class Solution:
    def spiralMatrixIII(self, rows: int, cols: int, rStart: int, cStart: int) -> List[List[int]]:
        dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        ans = []
        r, c = rStart, cStart
        if 0 <= r < rows and 0 <= c < cols:
            ans.append([r, c])

        step = 1

        while len(ans) < rows * cols:

            for d in range(4):
                dr, dc = dirs[d]

                for _ in range(step):
                    r += dr
                    c += dc

                    if 0 <= r < rows and 0 <= c < cols:
                        ans.append([r, c])
                        if len(ans) == rows * cols:
                            return ans

                if d % 2 == 1:
                    step += 1

        return ans