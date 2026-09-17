class Solution:
    def maxCoins(self, nums: list[int]) -> int:
        arr = [1] + nums + [1]
        n = len(arr)
        dp = {}

        def dfs(left, right):
            if left + 1 == right:
                return 0

            if (left, right) in dp:
                return dp[(left, right)]

            ans = 0

            for k in range(left + 1, right):
                coins = (dfs(left, k) + arr[left] * arr[k] * arr[right] + dfs(k, right))
                ans = max(ans, coins)

            dp[(left, right)] = ans

            return ans

        return dfs(0, n - 1)