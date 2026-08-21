class Solution:
    def rob(self, nums: List[int]) -> int:
        def rob198(arr):
            if len(arr) == 1:
                return arr[0]

            dp = [0] * len(arr)
            dp[0] = arr[0]
            dp[1] = max(arr[0], arr[1])

            for i in range(2, len(arr)):
                dp[i] = max(dp[i - 1], dp[i - 2] + arr[i])

            return dp[-1]

        n = len(nums)

        if n == 1:
            return nums[0]

        return max(rob198(nums[:-1]),rob198(nums[1:]))