class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)

        hold = [float("-inf")] * (n + 1)
        sold = [float("-inf")] * (n + 1)
        rest = [0] * (n + 1)

        for i in range(n):
            hold[i] = max(hold[i - 1], rest[i - 1] - prices[i])
            sold[i] = hold[i-1] + prices[i]
            rest[i] = max(rest[i - 1], sold[i - 1])

        return max(sold[n-1], rest[n-1])