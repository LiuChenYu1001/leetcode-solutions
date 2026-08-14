class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        n = 9

        row_seen = [[False] * n for _ in range(n)]
        col_seen = [[False] * n for _ in range(n)]
        box_seen = [[False] * n for _ in range(n)]

        for i in range(n):
            for j in range(n):
                val = board[i][j]
                
                if val == ".":
                    continue
                
                num = int(val) - 1

                box_index = (i // 3) * 3 + (j // 3)

                if row_seen[i][num] or col_seen[j][num] or box_seen[box_index][num]:
                    return False

                row_seen[i][num] = True
                col_seen[j][num] = True
                box_seen[box_index][num] = True

        return True