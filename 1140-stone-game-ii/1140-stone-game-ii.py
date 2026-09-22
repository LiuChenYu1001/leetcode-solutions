class Solution:
    def stoneGameII(self, piles: list[int]) -> int:
        n = len(piles)
        suffix = [0] * (n + 1)
        
        for i in range(n - 1, -1, -1):
            suffix[i] = suffix[i + 1] + piles[i]

        memo = {}

        def dp(i, M):
            if i + 2 * M >= n:
                return suffix[i]

            if (i, M) in memo:
                return memo[(i, M)]

            ans = 0

            for X in range(1, 2 * M + 1):
                opp = dp(i + X, max(M, X))
                curr = suffix[i] - opp

                ans = max(ans, curr)

            memo[(i, M)] = ans
            return ans

        return dp(0, 1)