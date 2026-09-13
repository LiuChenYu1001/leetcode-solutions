class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:
        n = len(stoneValue)
        stoneValue += [0, 0]
        dp = [0] * (n + 3)

        for i in range(n - 1, -1, -1):
            dp[i] = max(stoneValue[i] - dp[i + 1], 
                        stoneValue[i] + stoneValue[i + 1] - dp[i + 2], 
                        stoneValue[i] + stoneValue[i + 1] + stoneValue[i + 2] - dp[i + 3])

        if dp[0] > 0:
            return "Alice"
        elif dp[0] < 0:
            return "Bob"
        else:
            return "Tie"