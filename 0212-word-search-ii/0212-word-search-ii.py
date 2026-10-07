class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        trie = {}

        for word in words:
            node = trie

            for ch in word:
                if ch not in node:
                    node[ch] = {}

                node = node[ch]

            node["word"] = word

        m, n = len(board), len(board[0])
        ans = []

        def dfs(r, c, node):
            if r < 0 or r >= m or c < 0 or c >= n:
                return

            ch = board[r][c]

            if ch == "#" or ch not in node:
                return

            node = node[ch]

            if "word" in node:
                ans.append(node["word"])
                del node["word"]

            board[r][c] = "#"

            dfs(r - 1, c, node)
            dfs(r + 1, c, node)
            dfs(r, c - 1, node)
            dfs(r, c + 1, node)

            board[r][c] = ch

        for i in range(m):
            for j in range(n):
                dfs(i, j, trie)

        return ans

        # Trie