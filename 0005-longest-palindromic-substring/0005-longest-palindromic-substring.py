class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        dp = [[False] * n for _ in range(n)]

        start = 0
        max_len = 1

        for i in range(n - 1, -1, -1):
            for j in range(i, n):

                if s[i] == s[j]:
                    if j - i <= 2:
                        dp[i][j] = True
                    else:
                        dp[i][j] = dp[i + 1][j - 1]

                if dp[i][j] and j - i + 1 > max_len:
                    start = i
                    max_len = j - i + 1

        return s[start:start + max_len]