class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        total = sum(nums)

        if abs(target) > total:
            return 0

        if (total + target) % 2:
            return 0

        p = (total + target) // 2
        dp = [0] * (p + 1)
        dp[0] = 1

        for num in nums:
            for j in range(p, num - 1, -1):
                dp[j] += dp[j - num]

        return dp[p]