class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m, n = len(board), len(board[0])

        start_word = word[0]
        prefix = set()
        for i in range(1, len(word) + 1):
            prefix.add(word[:i])

        start = []
        for i in range(m):
            for j in range(n):
                if board[i][j] == start_word:
                    start.append((i, j))

        def dfs(r, c, tem):
            if r < 0 or r >= m or c < 0 or c >= n:
                return False

            if board[r][c] == "#":
                return False

            temp = board[r][c]
            tem = tem + temp

            if tem not in prefix:
                return False

            if tem == word:
                return True

            board[r][c] = "#"

            down = dfs(r + 1, c, tem)
            up = dfs(r - 1, c, tem)
            right = dfs(r, c + 1, tem)
            left = dfs(r, c - 1, tem)

            board[r][c] = temp

            return up or down or left or right

        for i, j in start:
            if dfs(i, j, ""):
                return True

        return False