class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        increase = decrease = 0
        ans = 1
        n = len(nums)

        for i in range(1, n):
            if nums[i] > nums[i - 1]:
                increase += 1
                ans = max(ans, increase + 1)
            else:
                increase = 0

        for j in range(1, n):
            if nums[j] < nums[j - 1]:
                decrease += 1
                ans = max(ans, decrease + 1)
            else:
                decrease = 0

        return ans